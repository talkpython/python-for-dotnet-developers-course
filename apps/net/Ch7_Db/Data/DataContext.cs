using Microsoft.EntityFrameworkCore;

namespace Ch7_Db.Data
{
    public class AppDbContext : DbContext
    {
        public DbSet<Guitar> Guitars { get; set; }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            optionsBuilder.UseSqlServer(
                @"Server=LOCALHOST\SQLEXPRESS;Database=guitars;Trusted_Connection=Yes");
            
        }
    }
}