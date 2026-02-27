using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Logging;
using assignement4.Services;

namespace assignement4.Controllers
{
    public class HomeController : Controller
    {
        private readonly IConfiguration _configuration;
        private readonly IMessageService _messageService;
        private readonly ILogger<HomeController> _logger;

        public HomeController(
            IConfiguration configuration,
            IMessageService messageService,
            ILogger<HomeController> logger)
        {
            _configuration = configuration;
            _messageService = messageService;
            _logger = logger;
        }

        public IActionResult Index()
        {
            // Read from appsettings
            var appName = _configuration["AppSettings:AppName"];
            var version = _configuration["AppSettings:Version"];

            // Log message
            _logger.LogInformation("Home Page Loaded");

            ViewBag.AppName = appName;
            ViewBag.Version = version;
            ViewBag.ServiceMessage = _messageService.GetMessage();

            return View();
        }
    }
}
