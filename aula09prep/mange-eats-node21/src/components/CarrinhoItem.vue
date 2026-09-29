<template>
  <div class="flex flex-col gap-4 border-b border-stone-200 py-5 last:border-0 sm:flex-row sm:items-center">
    <div class="grid h-20 w-20 shrink-0 place-items-center rounded-2xl bg-orange-50 text-4xl">{{ item.emoji }}</div>
    <div class="min-w-0 flex-1">
      <h3 class="font-bold text-stone-900">{{ item.nome }}</h3>
      <p class="mt-1 text-sm text-stone-500">{{ formatarMoeda(item.preco) }} cada</p>
    </div>
    <div class="flex items-center justify-between gap-4 sm:justify-end">
      <div class="flex items-center overflow-hidden rounded-xl border border-stone-300">
        <button class="h-10 w-10 font-bold hover:bg-stone-100" @click="$emit('diminuir', item.id)">−</button>
        <span class="grid h-10 min-w-10 place-items-center border-x border-stone-300 font-semibold">{{ item.quantidade }}</span>
        <button class="h-10 w-10 font-bold hover:bg-stone-100" @click="$emit('aumentar', item.id)">+</button>
      </div>
      <strong class="min-w-24 text-right text-red-700">{{ formatarMoeda(item.preco * item.quantidade) }}</strong>
      <button class="text-sm font-semibold text-stone-400 hover:text-red-700" @click="$emit('remover', item.id)">Remover</button>
    </div>
  </div>
</template>

<script setup>
defineProps({ item: { type: Object, required: true } })
defineEmits(['aumentar', 'diminuir', 'remover'])

function formatarMoeda(valor) {
  return new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(valor)
}
</script>
