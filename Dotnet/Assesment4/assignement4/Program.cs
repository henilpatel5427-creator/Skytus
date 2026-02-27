using assignement4.Services;

var builder = WebApplication.CreateBuilder(args);

// Add MVC
builder.Services.AddControllersWithViews();

// Register Custom Service
builder.Services.AddScoped<IMessageService, MessageService>();

var app = builder.Build();

// Custom Middleware
app.Use(async (context, next) =>
{
    Console.WriteLine("Request Path: " + context.Request.Path);
    await next();
});

if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Home/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();
app.UseRouting();
app.UseAuthorization();

app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Home}/{action=Index}/{id?}");

app.Run();
