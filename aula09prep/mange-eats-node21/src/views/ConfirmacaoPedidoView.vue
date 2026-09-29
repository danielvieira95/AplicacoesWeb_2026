<template>
  <div class="page-shell">
    <Navbar />
    <main class="container-page py-12">
      <div class="mx-auto max-w-2xl card-base overflow-hidden">
        <div class="bg-red-700 px-8 py-10 text-center text-white">
          <div class="mx-auto grid h-20 w-20 place-items-center rounded-full bg-white text-4xl text-red-700">✓</div>
          <h1 class="mt-5 text-3xl font-black">Pedido confirmado!</h1>
          <p class="mt-2 text-red-100">Recebemos seu pedido e ele já está sendo preparado.</p>
        </div>

        <div v-if="pedido" class="p-8">
          <div class="grid gap-4 rounded-2xl bg-stone-50 p-5 sm:grid-cols-2">
            <div><p class="text-xs font-bold uppercase text-stone-400">Pedido</p><p class="mt-1 font-black">#{{ pedido.numero }}</p></div>
            <div><p class="text-xs font-bold uppercase text-stone-400">Pagamento</p><p class="mt-1 font-black">{{ pedido.cliente.pagamento }}</p></div>
            <div><p class="text-xs font-bold uppercase text-stone-400">Cliente</p><p class="mt-1 font-semibold">{{ pedido.cliente.nome }}</p></div>
            <div><p class="text-xs font-bold uppercase text-stone-400">Total</p><p class="mt-1 font-black text-red-700">{{ moeda(pedido.total) }}</p></div>
          </div>
          <div class="mt-6">
            <p class="text-sm font-bold uppercase text-stone-400">Entrega em</p>
            <p class="mt-1 font-semibold">{{ pedido.cliente.endereco }}</p>
          </div>
          <router-link to="/cardapio" class="btn-primary mt-8 w-full">Fazer novo pedido</router-link>
        </div>

        <div v-else class="p-8 text-center">
          <p class="text-stone-500">Nenhum pedido foi finalizado nesta sessão.</p>
          <router-link to="/cardapio" class="btn-primary mt-5">Ir para o cardápio</router-link>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import Navbar from '../components/Navbar.vue'
import { useCarrinhoStore } from '../stores/carrinho'

const carrinho = useCarrinhoStore()
const pedido = carrinho.ultimoPedido

function moeda(valor) {
  return new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(valor)
}
</script>
