import axios from 'axios';

const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000',
  headers: {
    'Content-Type': 'application/json',
    // This simulates the user being logged in, as per the backend dependency.
    // In a real app, this would be handled by an auth flow (e.g., setting a token).
    'X-User-Id': 1,
  },
});

export default {
  getTickets() {
    return apiClient.get('/api/v1/tickets/');
  },
  createTicket(ticketData) {
    return apiClient.post('/api/v1/tickets/', ticketData);
  },
  // Add other ticket-related API calls here
  // getTicket(id) { ... }
};
