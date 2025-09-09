-- position, category, vacancy, area, skill

CREATE TABLE IF NOT EXISTS "skill" (
  "id" INT AUTO_INCREMENT PRIMARY KEY,
  "name" VARCHAR(100)
  );

CREATE TABLE IF NOT EXISTS "main_vacancy" (
  "id" INT AUTO_INCREMENT,
  "vacancy_id" BIG INT,
  "min_salary" DECIMAL(10,2),
  "max_salary" DECIMAL(10,2),
);

CREATE TABLE IF NOT EXISTS "vacancy_skill" (
  "id" INT AUTO_INCREMENT PRIMARY KEY,
  "skill_id" INT,
  "main_vacancy_id"  INT,
  FOREIGN KEY ("skill_id") REFERENCES "skills"("id"),
  FOREIGN KEY ("main_vacancy_id") REFERENCES "main_vacancy"("id")
  );

