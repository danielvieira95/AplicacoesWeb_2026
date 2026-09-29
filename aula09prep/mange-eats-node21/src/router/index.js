import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue'
import CadastroView from '../views/CadastroView.vue'
import CardapioView from '../views/CardapioView.vue'
import CarrinhoView from '../views/CarrinhoView.vue'
import ConfirmacaoPedidoView from '../views/ConfirmacaoPedidoView.vue'

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', name: 'login', component: LoginView },
  { path: '/cadastro', name: 'cadastro', component: CadastroView },
  { path: '/cardapio', name: 'cardapio', component: CardapioView },
  { path: '/carrinho', name: 'carrinho', component: CarrinhoView },
  { path: '/confirmacao', name: 'confirmacao', component: ConfirmacaoPedidoView },
]

export default createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior: () => ({ top: 0 }),
})
