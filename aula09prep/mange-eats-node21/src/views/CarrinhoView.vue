<template>
  <div class="page-shell">
    <Navbar />
    <main class="container-page py-10">
      <div class="mb-8">
        <p class="text-sm font-bold uppercase tracking-[.18em] text-red-700">Seu pedido</p>
        <h1 class="mt-2 text-3xl font-black">Carrinho</h1>
      </div>

      <div v-if="!carrinho.itens.length" class="card-base p-10 text-center">
        <div class="text-7xl">🛒</div>
        <h2 class="mt-5 text-2xl font-black">Seu carrinho está vazio</h2>
        <p class="mt-2 text-stone-500">Escolha alguns produtos do cardápio para começar.</p>
        <router-link to="/cardapio" class="btn-primary mt-6">Ver cardápio</router-link>
      </div>

      <div v-else class="grid gap-8 lg:grid-cols-[1fr_360px]">
        <section class="card-base p-6">
          <CarrinhoItem v-for="item in carrinho.itens" :key="item.id" :item="item" @aumentar="carrinho.aumentar" @diminuir="carrinho.diminuir" @remover="carrinho.remover" />
        </section>

        <aside class="card-base h-fit p-6 lg:sticky lg:top-24">
          <h2 class="text-xl font-black">Resumo do pedido</h2>
          <div class="mt-5 space-y-3 text-sm">
            <div class="flex justify-between"><span class="text-stone-500">Subtotal</span><span>{{ moeda(carrinho.subtotal) }}</span></div>
            <div class="flex justify-between"><span class="text-stone-500">Entrega</span><span>{{ moeda(carrinho.taxaEntrega) }}</span></div>
            <div class="flex justify-between border-t border-stone-200 pt-4 text-lg font-black"><span>Total</span><span class="text-red-700">{{ moeda(carrinho.total) }}</span></div>
          </div>

          <div class="mt-6 space-y-4">
            <div>
              <label class="mb-2 block text-sm font-semibold">Nome para o pedido</label>
              <input v-model="cliente.nome" class="input-base" placeholder="Seu nome" />
            </div>
            <div>
              <label class="mb-2 block text-sm font-semibold">Endereço de entrega</label>
              <input v-model="cliente.endereco" class="input-base" placeholder="Rua, número, bairro" />
            </div>
            <div>
              <label class="mb-2 block text-sm font-semibold">Forma de pagamento</label>
              <select v-model="cliente.pagamento" class="input-base">
                <option>Pix</option>
                <option>Cartão</option>
                <option>Dinheiro</option>
              </select>
            </div>
            <p v-if="erro" class="text-sm font-medium text-red-700">{{ erro }}</p>
            <button class="btn-primary w-full" @click="finalizar">Finalizar pedido</button>
            <router-link to="/cardapio" class="btn-secondary w-full">Continuar comprando</router-link>
          </div>
        </aside>
      </div>
    </main>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import Navbar from '../components/Navbar.vue'
import CarrinhoItem from '../components/CarrinhoItem.vue'
import { useCarrinhoStore } from '../stores/carrinho'

const carrinho = useCarrinhoStore()
const router = useRouter()
const erro = ref('')
const cliente = reactive({ nome: '', endereco: '', pagamento: 'Pix' })

function moeda(valor) {
  return new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(valor)
}

function finalizar() {
  erro.value = ''
  if (!cliente.nome || !cliente.endereco) {
    erro.value = 'Informe nome e endereço para finalizar.'
    return
  }
  carrinho.finalizarPedido(cliente)
  router.push('/confirmacao')
}
</script>
