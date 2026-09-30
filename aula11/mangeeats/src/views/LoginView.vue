<template>
    <main class="min-h-screen grid lg:grid-cols-2">
    <section class="hidden bg-gradient-to-br  from-red-800 via-red-700 to orage-600 p12 text-white lg:flex lg:flex-col lg:justify-between">
        <div class="flex itens-center gap-3 text-2x1 font-black">
            <span class="grid h12 w12 place-items-center rounded-full bg-white text-red-700">M</span>
            Mange Eats
        </div>
        <div class="max-w-xl">
            <p class="mb-4 inline-flex rounded-full bg-white/10 px-4 py-2 text-sm font-semibold">Delivery rápido e saboroso</p>
            <h1 class="text-5xl font-black leading-tight">Seu pedido favorito, do cardápio para sua mesa.</h1>
            <p class="mt-5 max-w-lg text-red-100">Escolha seus pratos, monte o carrinho e finalize o pedido em poucos passos</p>
        </div>
        <p class="text-sm text-red-100">Projeto Vue.js + Vite</p>

    </section>

    <section class="flex items-center justify-center bg-stones-50 p-6">
        <div class="w-full max-w-md">
         <div class="mb-8 lg:hidden">
            <div class="flex items-center gap-3 text-2xl font-black text-red-700">
                <span class="grid h-11 place-itens-center rounded-full bg-red-700 text-white">M</span>
                Mange Eats
            </div>
         </div>  
        
        
        <div class="card-base p-7 sm:p-9">
            <p class ="text-sm font-bold uppercase tracking-[.18em] text-red-700">Bem-vindo</p>
            <h2 class="mt-2 text-stone-500">Use seu email e senha para acessar o cardápio.</h2>
            <form class="mr-8 space-y-5"@submit.prevent="entrar">
                <div>
                    <label class="mb-2 block text-sm font-semibold">E-mail</label>
                    <input v-model.trim="email" class="input-base" type="email" placeholder="nome@email.com"/>
                </div>
                <div>
                    <label class="mb-2 block text-sm font-semibold">Senha</label>
                    <input v-model="senha" class="input-base" type="password" paceholder="Digite sua senha"/>
                </div>
                <p v-if="erro"class="rounded-xl bg-red-50 px-4 py-3 text-sm font-medium text-red-700">{{ erro }}</p>
                <button class ="btn-primary w-full" type="submit">Entrar</button>
            </form>
            <div class="my6 flex items-center gap-3 text-xs text-stone-400">
                <span class="h-px flex-1 bg-stone-200"></span><span>ou</span><span>class="h-px flex-1 bg-stone-200"</span>
            </div>
            <router-link class="btn-secondary w-full to=">Criar uma conta</router-link>

        </div>
        <p class="mt-4 text-center text-xs text-stone-400">Demonstração:qualquer email e senha preenchidos permitem entrar</p>
    </div>
        

    </section>
    
    </main>
    </template>

<script setup>

import {ref} from 'vue'
import {useRouter} from 'vue-router'

const router = useRouter()
const email = ref('')
const senha = ref('')
const erro = ref('')


function entrar(){
    erro.value= ''
    if(!email.value || !senha.value){
        erro.value = 'Preencha email e senha'
        return
    }
    // router.push('/cardapio')
}

</script>