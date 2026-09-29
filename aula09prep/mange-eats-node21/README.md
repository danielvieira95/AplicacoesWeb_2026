# Mange Eats — Vue.js (Node 21)

Projeto frontend em Vue 3 + Vite, preparado para uso com **Node.js 21.x**.

## Stack

- Vue 3.5.13
- Vue Router 4.5.0
- Pinia 2.2.6
- Vite 5.4.11
- Tailwind CSS 3.4.17
- Axios 1.7.9

As versões foram fixadas para evitar que `npm install` puxe uma versão futura do Vite/Rolldown incompatível com o ambiente da aula.

## Como executar

```bash
node -v
npm -v
npm install
npm run dev
```

Acesse o endereço mostrado pelo Vite, normalmente:

```text
http://localhost:5173
```

## Telas

- LoginView.vue
- CadastroView.vue
- CardapioView.vue
- CarrinhoView.vue
- ConfirmacaoPedidoView.vue

## Componentes

- Navbar.vue
- ProdutoCard.vue
- CarrinhoItem.vue

## Observação

O login e os produtos são simulados no frontend. O projeto pode ser conectado posteriormente a uma API Spring Boot ou Django REST Framework usando Axios.
