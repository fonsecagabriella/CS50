CREATE INDEX "search_enrollmenst_by_student" ON "enrollments"("student_id");

CREATE INDEX "search_enrollments_by_course_id" ON "enrollments"("course_id");

CREATE INDEX "search_course_department" ON "courses"("department");

CREATE INDEx "search_course_semester" ON "courses"("semester");