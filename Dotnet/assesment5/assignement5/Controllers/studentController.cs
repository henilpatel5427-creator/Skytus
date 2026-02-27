using Microsoft.AspNetCore.Mvc;
using assignement5.Models;
using System.Collections.Generic;

namespace assignement5.Controllers
{
    public class StudentController : Controller
    {
        public IActionResult Index()
        {
            var students = new List<Student>
            {
                new Student { StudentId = 1, Name = "Henil", Department = "CE", Marks = 85 },
                new Student { StudentId = 2, Name = "Raj", Department = "IT", Marks = 72 },
                new Student { StudentId = 3, Name = "Priya", Department = "CE", Marks = 90 }
            };

            return View(students);
        }
    }
}
