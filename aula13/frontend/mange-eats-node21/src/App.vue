<script setup>

import {ref, onMounted} from "vue";
import api from "./services/api";

// Lista reativa de produtos

const produtos = ref([]);
// Dados do formulário
const nome = ref("");
const quantidade = ref(0);
const preco = ref(0);
const erro = ref("");

// GET - Listar produtos

async function listarProdutos(){
  try {
    const resposta = await api.get("produtos/");
    produtos.value = resposta.data;
    erro.value = "";
  } catch (error){
    console.error(error);
    erro.value = "Erro ao buscar produtos";
  }
}


// Post Cadastrar produto 


async  function cadastrarProduto(){
  try {
    const novoProduto = {
      nome: nome.value,
      quantidade : Number(quantidade.value),
      preco: Number(preco.value)
    };

    await api.post("produtos/",novoProduto);

    // Limpar o formulário
    nome.value = "";
    quantidade.value = 0;
    preco.value = 0;

    // Atualizar a lista de produtos

    await listarProdutos();

  }catch(error){
       console.error(error.response?.data ?? error);
      error.value = "Erro ao cadastrar produto";
    }
  }


  // Executado quando o componente é montado 
  onMounted(()=>{
    listarProdutos();
  });


</script>

<template>
  <main>
    <h1>
      Cadastro de Produtos </h1>
      <form @submit.prevent="cadastrarProduto">
        <input v-model="nome" placeholder="Nome" required/>
        <input 
        v-model.number= "quantidade"
        type="number"
        min="0"
        required
        />

        <input
        v-model.number="preco"
        type="number"
        min="0"
        step="0.01"
        required
        />
        <button type = "submit">Cadastrar</button>
      </form>
      <p v-if="erro">{{ erro }}</p>
      <h2>Produtos Cadastrados</h2>
      <ul>
      <li v-for="produto in produtos":key="produto.id">
        {{ 
          
          produto.nome
          
          }}- R$ {{produto.preco}} - Quantidade: {{ produto.quantidade }}
      </li>

      </ul>
  </main>
</template>
