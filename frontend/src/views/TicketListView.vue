<template>
  <v-card>
    <v-card-title>Tickets</v-card-title>
    <v-card-text>
      <v-data-table
        :headers="headers"
        :items="tickets"
        :loading="loading"
        class="elevation-1"
      >
        <template v-slot:item.status="{ item }">
          <v-chip :color="getStatusColor(item.raw.status)" dark small>
            {{ item.raw.status }}
          </v-chip>
        </template>
      </v-data-table>
    </v-card-text>
  </v-card>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import apiClient from '@/api';

const loading = ref(true);
const tickets = ref([]);
const headers = ref([
  { title: 'ID', key: 'id', align: 'start' },
  { title: 'Title', key: 'title' },
  { title: 'Status', key: 'status' },
  { title: 'Priority', key: 'priority' },
  { title: 'Owner', key: 'owner.email' },
  { title: 'Created At', key: 'created_at' },
]);

onMounted(async () => {
  loading.value = true;
  try {
    const response = await apiClient.getTickets();
    tickets.value = response.data;
  } catch (error) {
    console.error('There was an error fetching the tickets:', error);
    // Here you could show a snackbar or toast notification
  } finally {
    loading.value = false;
  }
});

const getStatusColor = (status) => {
  switch (status) {
    case 'OPEN':
      return 'blue';
    case 'IN_PROGRESS':
      return 'orange';
    case 'CLOSED':
      return 'green';
    default:
      return 'grey';
  }
};
</script>
