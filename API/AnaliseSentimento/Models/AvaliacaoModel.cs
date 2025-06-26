namespace AnaliseSentimento.Models
{
    public class AvaliacaoModel
    {
        public Guid Id { get; set; }
        public string? Comentario { get; set; }
        public string? Sentimento { get; set; }
        public DateTime DataAvaliacao { get; set; } = DateTime.UtcNow;
    }
}
