import { createRouter, createWebHistory } from 'vue-router';
import TicketListView from '../views/TicketListView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'tickets',
      component: TicketListView,
    },
    // Future routes can be added here
    // {
    //   path: '/tickets/:id',
    //   name: 'ticket-detail',
    //   component: () => import('../views/TicketDetailView.vue')
    // },
  ],
});

export default router;
