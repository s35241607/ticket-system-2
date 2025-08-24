<template>
  <v-card>
    <v-card-title class="d-flex justify-space-between align-center">
      <span>Tickets</span>
      <v-btn color="primary" @click="dialog = true">
        <v-icon left>mdi-plus</v-icon>
        New Ticket
      </v-btn>
    </v-card-title>
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

  <create-ticket-dialog
    v-model="dialog"
    @ticket-created="handleTicketCreated"
  />
</template>

<script setup>
import { ref, onMounted } from 'vue';
import apiClient from '@/api';
import CreateTicketDialog from '@/components/CreateTicketDialog.vue';

const loading = ref(true);
const tickets = ref([]);
const dialog = ref(false);

const headers = ref([
  { title: 'ID', key: 'id', align: 'start' },
  { title: 'Title', key: 'title' },
  { title: 'Status', key: 'status' },
  { title: 'Priority', key: 'priority' },
  { title: 'Owner', key: 'owner.email' },
  { title: 'Created At', key: 'created_at' },
]);

const fetchTickets = async () => {
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
};

onMounted(fetchTickets);

const handleTicketCreated = (newTicket) => {
  // Option 1: Add to the list directly (more responsive)
  tickets.value.push(newTicket);
  // Option 2: Re-fetch the whole list
  // fetchTickets();
};

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
