using Microsoft.EntityFrameworkCore;
using TicketSystem.Api.Models;

namespace TicketSystem.Api.Data
{
    public class AppDbContext : DbContext
    {
        public AppDbContext(DbContextOptions<AppDbContext> options) : base(options)
        {
        }

        public DbSet<Ticket> Tickets { get; set; }
        public DbSet<User> Users { get; set; }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);

            // Configure the one-to-many relationship between User and Ticket
            modelBuilder.Entity<User>()
                .HasMany(u => u.Tickets)
                .WithOne(t => t.Owner)
                .HasForeignKey(t => t.OwnerId)
                .OnDelete(DeleteBehavior.Restrict); // Or Cascade, depending on your needs
        }
    }
}
