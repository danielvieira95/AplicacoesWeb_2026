<template>
  <header class="sticky top-0 z-40 border-b border-red-800 bg-red-700 text-white shadow-sm">
    <div class="container-page flex h-16 items-center justify-between gap-4">
      <router-link to="/cardapio" class="flex items-center gap-3 font-black tracking-tight">
        <span class="grid h-10 w-10 place-items-center rounded-full bg-white text-xl text-red-700">M</span>
        <span class="text-xl">Mange Eats</span>
      </router-link>

      <nav class="flex items-center gap-2 sm:gap-5">
        <router-link to="/cardapio" class="hidden font-medium hover:text-orange-200 sm:block">Cardápio</router-link>
        <router-link to="/carrinho" class="relative rounded-xl bg-white/10 px-3 py-2 font-semibold hover:bg-white/20">
          🛒 Carrinho
          <span v-if="carrinho.quantidadeTotal" class="ml-1 rounded-full bg-orange-500 px-2 py-0.5 text-xs text-white">
            {{ carrinho.quantidadeTotal }}
          </span>
        </router-link>
        <router-link to="/login" class="hidden rounded-xl border border-white/30 px-3 py-2 text-sm font-semibold hover:bg-white/10 md:block">Sair</router-link>
      </nav>
    </div>
  </header>
</template>

<script setup>
import { useCarrinhoStore } from '../stores/carrinho'
const carrinho = useCarrinhoStore()
</script>
