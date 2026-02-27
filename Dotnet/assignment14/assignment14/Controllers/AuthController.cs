using Microsoft.AspNetCore.Mvc;
using assignment14.Services;

namespace assignment14.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class AuthController : ControllerBase
    {
        private readonly EmailService _emailService;

        public AuthController(EmailService emailService)
        {
            _emailService = emailService;
        }

        public class LoginModel
        {
            public string Email { get; set; } = string.Empty;
            public string Password { get; set; } = string.Empty;
        }

        [HttpPost("login")]
        public IActionResult Login([FromBody] LoginModel model)
        {
            if (string.IsNullOrEmpty(model.Email))
                return BadRequest("Email is required");

            _emailService.SendEmail(
                model.Email,
                "Login Successful",
                "You have successfully logged in to Assignment14."
            );

            return Ok("Login successful. Email sent.");
        }
    }
}