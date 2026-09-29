<template>
  <div class="page-shell">
    <Navbar />
    <section class="bg-gradient-to-r from-red-800 to-red-600 text-white">
      <div class="container-page grid gap-8 py-12 lg:grid-cols-[1.3fr_.7fr] lg:items-center">
        <div>
          <p class="text-sm font-bold uppercase tracking-[.2em] text-orange-200">Mange Eats</p>
          <h1 class="mt-3 text-4xl font-black sm:text-5xl">O sabor que chega até você.</h1>
          <p class="mt-4 max-w-2xl text-red-100">Hambúrgueres, porções, bebidas e sobremesas preparados para deixar seu pedido completo.</p>
        </div>
        <div class="hidden justify-self-end rounded-3xl bg-white/10 p-6 text-8xl lg:block">🍔</div>
      </div>
    </section>

    <main class="container-page py-10">
      <div class="mb-8 flex flex-col gap-4 lg:flex-row lg:items-end lg:justify-between">
        <div>
          <p class="text-sm font-bold text-red-700">NOSSO CARDÁPIO</p>
          <h2 class="mt-1 text-3xl font-black">Escolha o que vai pedir hoje</h2>
        </div>
        <div class="flex flex-wrap gap-2">
          <button v-for="categoria in categorias" :key="categoria" class="rounded-full px-4 py-2 text-sm font-semibold transition" :class="categoriaAtiva === categoria ? 'bg-red-700 text-white' : 'border border-stone-300 bg-white hover:bg-stone-100'" @click="categoriaAtiva = categoria">
            {{ categoria }}
          </button>
        </div>
      </div>

      <div class="grid gap-6 sm:grid-cols-2 xl:grid-cols-3">
        <ProdutoCard v-for="produto in produtosFiltrados" :key="produto.id" :produto="produto" @adicionar="adicionar" />
      </div>

      <div v-if="toast" class="fixed bottom-6 right-6 z-50 rounded-xl bg-stone-900 px-5 py-3 font-semibold text-white shadow-xl">{{ toast }}</div>
    </main>
  </div>
</template>

<script setup>
import { computed, ref } from 'vue'
import Navbar from '../components/Navbar.vue'
import ProdutoCard from '../components/ProdutoCard.vue'
import { useCarrinhoStore } from '../stores/carrinho'

const carrinho = useCarrinhoStore()
const categoriaAtiva = ref('Todos')
const toast = ref('')
let toastTimer

const produtos = [
  { id: 1, nome: 'Mange Bacon', categoria: 'Hambúrgueres', descricao: 'Pão brioche, hambúrguer artesanal, queijo, bacon crocante e molho da casa.', preco: 32.90, nota: '4,9', emoji: '🍔' },
  { id: 2, nome: 'Cheese Salada', categoria: 'Hambúrgueres', descricao: 'Carne artesanal, queijo, alface, tomate, cebola roxa e maionese especial.', preco: 28.90, nota: '4,8', emoji: '🥪' },
  { id: 3, nome: 'Batata Crocante', categoria: 'Porções', descricao: 'Batatas fritas sequinhas com páprica e molho especial à parte.', preco: 19.90, nota: '4,7', emoji: '🍟' },
  { id: 4, nome: 'Onion Rings', categoria: 'Porções', descricao: 'Anéis de cebola empanados e crocantes, servidos com molho barbecue.', preco: 22.90, nota: '4,7', emoji: '🧅' },
  { id: 5, nome: 'Refrigerante', categoria: 'Bebidas', descricao: 'Lata 350 ml. Escolha seu sabor favorito na observação do pedido.', preco: 7.00, nota: '4,9', emoji: '🥤' },
  { id: 6, nome: 'Milk-shake Chocolate', categoria: 'Bebidas', descricao: 'Milk-shake cremoso de chocolate com calda e chantilly.', preco: 18.90, nota: '4,9', emoji: '🥛' },
  { id: 7, nome: 'Brownie', categoria: 'Sobremesas', descricao: 'Brownie de chocolate servido com cobertura especial da casa.', preco: 14.90, nota: '4,8', emoji: '🍫' },
  { id: 8, nome: 'Sorvete', categoria: 'Sobremesas', descricao: 'Duas bolas de sorvete com calda de chocolate e confeitos.', preco: 13.50, nota: '4,8', emoji: '🍨' },
]

const categorias = ['Todos', 'Hambúrgueres', 'Porções', 'Bebidas', 'Sobremesas']
const produtosFiltrados = computed(() => categoriaAtiva.value === 'Todos' ? produtos : produtos.filter(p => p.categoria === categoriaAtiva.value))

function adicionar(produto) {
  carrinho.adicionar(produto)
  toast.value = `${produto.nome} adicionado ao carrinho.`
  clearTimeout(toastTimer)
  toastTimer = setTimeout(() => toast.value = '', 1800)
}
</script>
