import { computed, ref } from 'vue'
import { defineStore } from 'pinia'

export const useCarrinhoStore = defineStore('carrinho', () => {
  const itens = ref([])
  const ultimoPedido = ref(null)

  const quantidadeTotal = computed(() =>
    itens.value.reduce((total, item) => total + item.quantidade, 0)
  )

  const subtotal = computed(() =>
    itens.value.reduce((total, item) => total + item.preco * item.quantidade, 0)
  )

  const taxaEntrega = computed(() => (itens.value.length ? 6.9 : 0))
  const total = computed(() => subtotal.value + taxaEntrega.value)

  function adicionar(produto) {
    const existente = itens.value.find((item) => item.id === produto.id)
    if (existente) existente.quantidade += 1
    else itens.value.push({ ...produto, quantidade: 1 })
  }

  function aumentar(id) {
    const item = itens.value.find((item) => item.id === id)
    if (item) item.quantidade += 1
  }

  function diminuir(id) {
    const item = itens.value.find((item) => item.id === id)
    if (!item) return
    if (item.quantidade > 1) item.quantidade -= 1
    else remover(id)
  }

  function remover(id) {
    itens.value = itens.value.filter((item) => item.id !== id)
  }

  function finalizarPedido(dadosCliente) {
    ultimoPedido.value = {
      numero: Math.floor(1000 + Math.random() * 9000),
      data: new Date().toLocaleString('pt-BR'),
      itens: itens.value.map((item) => ({ ...item })),
      subtotal: subtotal.value,
      taxaEntrega: taxaEntrega.value,
      total: total.value,
      cliente: { ...dadosCliente },
    }
    itens.value = []
    return ultimoPedido.value
  }

  return {
    itens,
    ultimoPedido,
    quantidadeTotal,
    subtotal,
    taxaEntrega,
    total,
    adicionar,
    aumentar,
    diminuir,
    remover,
    finalizarPedido,
  }
})
