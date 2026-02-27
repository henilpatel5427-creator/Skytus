using assignment8.Data;
using assignment8.Models;
using System.Collections.Generic;
using System.Linq;

namespace assignment8.Repositories
{
    public class StudentRepository : IStudentRepository
    {
        private readonly ApplicationDbContext _context;

        public StudentRepository(ApplicationDbContext context)
        {
            _context = context;
        }

        public IEnumerable<Student> GetAll()
        {
            return _context.Students
                           .OrderByDescending(s => s.Marks)
                           .ToList();
        }

        public Student GetById(int id)
        {
            return _context.Students.FirstOrDefault(s => s.Id == id);
        }

        public void Add(Student student)
        {
            _context.Students.Add(student);
        }

        public void Update(Student student)
        {
            _context.Students.Update(student);
        }

        public void Delete(int id)
        {
            var student = _context.Students.Find(id);
            _context.Students.Remove(student);
        }

        public void Save()
        {
            _context.SaveChanges();
        }
    }
}
