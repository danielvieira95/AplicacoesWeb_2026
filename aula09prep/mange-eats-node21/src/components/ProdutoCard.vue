<template>
  <article class="card-base overflow-hidden transition hover:-translate-y-1 hover:shadow-xl">
    <div class="flex h-40 items-center justify-center bg-gradient-to-br from-orange-50 to-red-50 text-7xl">
      {{ produto.emoji }}
    </div>
    <div class="p-5">
      <div class="mb-2 flex items-start justify-between gap-3">
        <div>
          <p class="text-xs font-bold uppercase tracking-wider text-red-700">{{ produto.categoria }}</p>
          <h3 class="mt-1 text-xl font-bold text-stone-900">{{ produto.nome }}</h3>
        </div>
        <span class="rounded-full bg-orange-100 px-2 py-1 text-xs font-bold text-orange-700">★ {{ produto.nota }}</span>
      </div>
      <p class="min-h-12 text-sm leading-6 text-stone-500">{{ produto.descricao }}</p>
      <div class="mt-5 flex items-center justify-between gap-3">
        <span class="text-xl font-black text-red-700">{{ formatarMoeda(produto.preco) }}</span>
        <button class="btn-primary px-4 py-2.5" @click="$emit('adicionar', produto)">Adicionar</button>
      </div>
    </div>
  </article>
</template>

<script setup>
defineProps({ produto: { type: Object, required: true } })
defineEmits(['adicionar'])

function formatarMoeda(valor) {
  return new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(valor)
}
</script>
