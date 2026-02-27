namespace assignment14.Services
{
    public class SmsService
    {
        private readonly ILogger<SmsService> _logger;

        public SmsService(ILogger<SmsService> logger)
        {
            _logger = logger;
        }

        public void SendSms(string number, string message)
        {
            try
            {
                _logger.LogInformation($"SMS sent to {number}");
                _logger.LogInformation($"Message: {message}");
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "SMS sending failed");
            }
        }
    }
}