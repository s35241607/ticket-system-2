<template>
  <v-dialog :model-value="modelValue" @update:model-value="$emit('update:modelValue', $event)" max-width="600px">
    <v-card>
      <v-card-title>
        <span class="headline">Create New Ticket</span>
      </v-card-title>
      <v-card-text>
        <v-form ref="form" v-model="valid">
          <v-text-field
            v-model="ticket.title"
            label="Title"
            :rules="[v => !!v || 'Title is required']"
            required
          ></v-text-field>
          <v-textarea
            v-model="ticket.description"
            label="Description"
          ></v-textarea>
          <v-select
            v-model="ticket.priority"
            :items="['LOW', 'MEDIUM', 'HIGH']"
            label="Priority"
            required
          ></v-select>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" text @click="$emit('update:modelValue', false)">Cancel</v-btn>
        <v-btn color="blue darken-1" :disabled="!valid" @click="save">Save</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup>
import { ref, reactive, defineEmits, defineProps } from 'vue';
import apiClient from '@/api';

const props = defineProps({
  modelValue: Boolean,
});

const emit = defineEmits(['update:modelValue', 'ticket-created']);

const valid = ref(false);
const form = ref(null);
const ticket = reactive({
  title: '',
  description: '',
  priority: 'MEDIUM',
});

const save = async () => {
  const { valid: isValid } = await form.value.validate();
  if (!isValid) return;

  try {
    const response = await apiClient.createTicket(ticket);
    emit('ticket-created', response.data);
    emit('update:modelValue', false);
    // Reset form
    ticket.title = '';
    ticket.description = '';
    ticket.priority = 'MEDIUM';
    form.value.resetValidation();
  } catch (error) {
    console.error('Failed to create ticket:', error);
    // Here you could show an error message to the user
  }
};
</script>
