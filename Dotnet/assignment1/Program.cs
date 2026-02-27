using System;
using System.Collections.Generic;
using System.Linq;

class StudentDetails
{
    public int student_id;
    public string name;
    public string department;
    public int marks;
}

class Program
{
    static void Main()
    {
        List<StudentDetails> students = new List<StudentDetails>();
        int choice;

        do
        {
            Console.WriteLine("\n===== STUDENT MENU =====");
            Console.WriteLine("1. Add Student");
            Console.WriteLine("2. Display All Students");
            Console.WriteLine("3. Display Name & Department");
            Console.WriteLine("4. Students with Marks > 75");
            Console.WriteLine("5. Students from Specific Department");
            Console.WriteLine("6. Sort by Marks (Descending)");
            Console.WriteLine("7. Display Top Scorer");
            Console.WriteLine("8. Exit");
            Console.Write("Enter choice: ");
            choice = Convert.ToInt32(Console.ReadLine());

            switch (choice)
            {
                case 1:
                    StudentDetails s = new StudentDetails();

                    Console.Write("Enter ID: ");
                    s.student_id = Convert.ToInt32(Console.ReadLine());

                    Console.Write("Enter Name: ");
                    s.name = Console.ReadLine();

                    Console.Write("Enter Department: ");
                    s.department = Console.ReadLine();

                    Console.Write("Enter Marks: ");
                    s.marks = Convert.ToInt32(Console.ReadLine());

                    students.Add(s);
                    Console.WriteLine("Student Added Successfully!");
                    break;

                case 2:
                    Console.WriteLine("\n--- All Students ---");
                    foreach (var item in students)
                    {
                        Console.WriteLine($"ID: {item.student_id}, Name: {item.name}, Dept: {item.department}, Marks: {item.marks}");
                    }
                    break;

                case 3:
                    Console.WriteLine("\n--- Name & Department ---");
                    foreach (var item in students)
                    {
                        Console.WriteLine($"Name: {item.name}, Dept: {item.department}");
                    }
                    break;

                case 4:
                    Console.WriteLine("\n--- Students with Marks > 75 ---");
                    foreach (var item in students)
                    {
                        if (item.marks > 75)
                        {
                            Console.WriteLine($"{item.name} - {item.marks}");
                        }
                    }
                    break;

                case 5:
                    Console.Write("Enter Department Name: ");
                    string dept = Console.ReadLine();

                    Console.WriteLine($"\n--- Students from {dept} ---");
                    foreach (var item in students)
                    {
                        if (item.department.Equals(dept, StringComparison.OrdinalIgnoreCase))
                        {
                            Console.WriteLine($"{item.name} - {item.department}");
                        }
                    }
                    break;

                case 6:
                    Console.WriteLine("\n--- Sorted by Marks (Descending) ---");
                    var sortedList = students.OrderByDescending(x => x.marks);
                    foreach (var item in sortedList)
                    {
                        Console.WriteLine($"{item.name} - {item.marks}");
                    }
                    break;

                case 7:
                    if (students.Count > 0)
                    {
                        var top = students.OrderByDescending(x => x.marks).First();
                        Console.WriteLine($"\nTop Scorer: {top.name} - {top.marks}");
                    }
                    else
                    {
                        Console.WriteLine("No students available.");
                    }
                    break;

                case 8:
                    Console.WriteLine("Exiting Program...");
                    break;

                default:
                    Console.WriteLine("Invalid Choice!");
                    break;
            }

        } while (choice != 8);
    }
}

