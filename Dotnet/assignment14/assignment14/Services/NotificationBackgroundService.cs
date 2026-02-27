using Microsoft.Extensions.Hosting;

namespace assignment14.Services
{
    public class NotificationBackgroundService : BackgroundService
    {
        private readonly ILogger<NotificationBackgroundService> _logger;
        private readonly IServiceScopeFactory _scopeFactory;

        public NotificationBackgroundService(
            ILogger<NotificationBackgroundService> logger,
            IServiceScopeFactory scopeFactory)
        {
            _logger = logger;
            _scopeFactory = scopeFactory;
        }

        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            _logger.LogInformation("Background Service Started");

            while (!stoppingToken.IsCancellationRequested)
            {
                try
                {
                    using var scope = _scopeFactory.CreateScope();

                    var emailService = scope.ServiceProvider.GetRequiredService<EmailService>();
                    var smsService = scope.ServiceProvider.GetRequiredService<SmsService>();

                    _logger.LogInformation("Running scheduled job...");

                    emailService.SendEmail("test@example.com",
                        "Assignment14 Notification",
                        "This email is sent every 1 minute.");

                    smsService.SendSms("9876543210",
                        "This SMS is sent every 1 minute.");

                    _logger.LogInformation("Scheduled job completed successfully");
                }
                catch (Exception ex)
                {
                    _logger.LogError(ex, "Error in background job");
                }

                await Task.Delay(TimeSpan.FromMinutes(1), stoppingToken);
            }
        }
    }
}