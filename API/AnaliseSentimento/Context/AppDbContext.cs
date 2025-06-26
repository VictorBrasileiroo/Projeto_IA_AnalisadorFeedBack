using AnaliseSentimento.Models;
using Microsoft.EntityFrameworkCore;

namespace AnaliseSentimento.Context
{
    public class AppDbContext : DbContext
    {
        public AppDbContext(DbContextOptions<AppDbContext> options) : base(options){}
        
        public DbSet<AvaliacaoModel> Avaliacoes { get; set; }
    }
}
