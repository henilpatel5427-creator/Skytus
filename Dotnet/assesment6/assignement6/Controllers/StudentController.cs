using Microsoft.AspNetCore.Mvc;
using assignement6.Models;
using System.Collections.Generic;
using System.Linq;

namespace assignement6.Controllers
{
    public class StudentController : Controller
    {
        // In-memory storage
        private static List<Student> students = new List<Student>();

        // READ
        public IActionResult Index()
        {
            return View(students);
        }

        // CREATE (GET)
        public IActionResult Create()
        {
            return View();
        }

        // CREATE (POST)
        [HttpPost]
        public IActionResult Create(Student student)
        {
            if (ModelState.IsValid)
            {
                student.Id = students.Count + 1;
                students.Add(student);
                return RedirectToAction("Index");
            }

            return View(student);
        }

        // EDIT (GET)
        public IActionResult Edit(int id)
        {
            var student = students.FirstOrDefault(s => s.Id == id);
            return View(student);
        }

        // EDIT (POST)
        [HttpPost]
        public IActionResult Edit(Student student)
        {
            if (ModelState.IsValid)
            {
                var existing = students.FirstOrDefault(s => s.Id == student.Id);

                existing.Name = student.Name;
                existing.Department = student.Department;
                existing.Marks = student.Marks;

                return RedirectToAction("Index");
            }

            return View(student);
        }

        // DELETE
        public IActionResult Delete(int id)
        {
            var student = students.FirstOrDefault(s => s.Id == id);
            students.Remove(student);
            return RedirectToAction("Index");
        }
    }
}
