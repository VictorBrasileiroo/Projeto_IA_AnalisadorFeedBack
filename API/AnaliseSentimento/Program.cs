using AnaliseSentimento.Context;
using AnaliseSentimento.Models;
using Microsoft.EntityFrameworkCore;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.

// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

builder.Services.AddDbContext<AppDbContext>(options =>
{
    options.UseSqlServer(builder.Configuration.GetConnectionString("DefaultConnection"));
});

var app = builder.Build();

app.MapPost("/avaliacoes", async (AvaliacaoModel avaliacao, AppDbContext db) =>
{

    db.Avaliacoes.Add(avaliacao);
    await db.SaveChangesAsync();
    return Results.Created($"/avaliacoes/{avaliacao.Id}", avaliacao);
});

app.MapGet("/avaliacoes", async (AppDbContext db) =>
{
    return await db.Avaliacoes.ToListAsync();
});

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.MapDelete("/avaliacoes/limpar", async (AppDbContext db) =>
{
    db.Avaliacoes.RemoveRange(db.Avaliacoes);
    await db.SaveChangesAsync();
    return Results.Ok("Todas as avaliações foram removidas.");
});

app.UseHttpsRedirection();

app.Run();
