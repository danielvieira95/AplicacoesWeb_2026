<template>
  <main class="min-h-screen bg-stone-50 py-10">
    <div class="mx-auto max-w-2xl px-4">
      <router-link to="/login" class="mb-6 inline-flex items-center gap-2 font-semibold text-red-700">← Voltar para o login</router-link>
      <div class="card-base overflow-hidden">
        <div class="bg-red-700 px-7 py-7 text-white">
          <p class="text-sm font-bold uppercase tracking-[.18em] text-red-100">Mange Eats</p>
          <h1 class="mt-2 text-3xl font-black">Crie sua conta</h1>
          <p class="mt-2 text-red-100">Cadastre seus dados para começar a fazer pedidos.</p>
        </div>
        <form class="grid gap-5 p-7 sm:grid-cols-2" @submit.prevent="cadastrar">
          <div class="sm:col-span-2">
            <label class="mb-2 block text-sm font-semibold">Nome completo</label>
            <input v-model="form.nome" class="input-base" placeholder="Seu nome" />
          </div>
          <div>
            <label class="mb-2 block text-sm font-semibold">E-mail</label>
            <input v-model="form.email" class="input-base" type="email" placeholder="nome@email.com" />
          </div>
          <div>
            <label class="mb-2 block text-sm font-semibold">Telefone</label>
            <input v-model="form.telefone" class="input-base" placeholder="(19) 99999-9999" />
          </div>
          <div class="sm:col-span-2">
            <label class="mb-2 block text-sm font-semibold">Endereço</label>
            <input v-model="form.endereco" class="input-base" placeholder="Rua, número e bairro" />
          </div>
          <div>
            <label class="mb-2 block text-sm font-semibold">Senha</label>
            <input v-model="form.senha" class="input-base" type="password" placeholder="Crie uma senha" />
          </div>
          <div>
            <label class="mb-2 block text-sm font-semibold">Confirmar senha</label>
            <input v-model="form.confirmacao" class="input-base" type="password" placeholder="Repita a senha" />
          </div>
          <p v-if="mensagem" class="sm:col-span-2 rounded-xl bg-orange-50 px-4 py-3 text-sm font-medium text-orange-800">{{ mensagem }}</p>
          <button class="btn-primary sm:col-span-2" type="submit">Cadastrar</button>
        </form>
      </div>
    </div>
  </main>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const mensagem = ref('')
const form = reactive({ nome: '', email: '', telefone: '', endereco: '', senha: '', confirmacao: '' })

function cadastrar() {
  if (!form.nome || !form.email || !form.senha) {
    mensagem.value = 'Preencha pelo menos nome, e-mail e senha.'
    return
  }
  if (form.senha !== form.confirmacao) {
    mensagem.value = 'As senhas não conferem.'
    return
  }
  router.push('/cardapio')
}
</script>
