from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=40)
    turnover = models.IntegerField()

    def __str__(self):
        return f"{self.name}"  # what to display in DB admin (instead of Object 1)

    class Meta:
        verbose_name_plural = "Companies"


class Employee(models.Model):
    POSITIONS = [
        ("A_position", "A_position"),
        ("B_position", "B_position"),
        ("C_position", "C_position"),
        ("D_position", "D_position"),
    ]

    LONGEST_POSITION_NAME = max([len(x) for (x, _) in POSITIONS])

    f_name = models.CharField(max_length=40)
    l_name = models.CharField(max_length=40)
    position = models.CharField(max_length=LONGEST_POSITION_NAME, choices=POSITIONS)
    date_of_birth = models.DateField()

    employer = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.f_name} {self.l_name}"
