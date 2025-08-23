namespace TicketSystem.Api.Models
{
    public class User
    {
        public int Id { get; set; }
        public required string Email { get; set; }
        public string? HashedPassword { get; set; } // Nullable for now
        public bool IsActive { get; set; } = true;

        public ICollection<Ticket> Tickets { get; set; } = new List<Ticket>();
    }
}
