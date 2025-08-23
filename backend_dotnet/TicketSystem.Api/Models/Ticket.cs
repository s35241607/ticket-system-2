using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace TicketSystem.Api.Models
{
    public class Ticket
    {
        public int Id { get; set; }

        [Required]
        [StringLength(100)]
        public required string Title { get; set; }

        [StringLength(500)]
        public string? Description { get; set; }

        public TicketStatus Status { get; set; } = TicketStatus.OPEN;
        public TicketPriority Priority { get; set; } = TicketPriority.MEDIUM;

        public DateTime CreatedAt { get; set; } = DateTime.UtcNow;
        public DateTime? UpdatedAt { get; set; }

        public int OwnerId { get; set; }
        [ForeignKey("OwnerId")]
        public User? Owner { get; set; }

        public int? ApproverId { get; set; }
        [ForeignKey("ApproverId")]
        public User? Approver { get; set; }
    }

    public enum TicketStatus
    {
        OPEN,
        IN_PROGRESS,
        CLOSED
    }

    public enum TicketPriority
    {
        LOW,
        MEDIUM,
        HIGH
    }
}
