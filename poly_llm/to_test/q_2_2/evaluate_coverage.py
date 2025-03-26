from poly_llm.common.abstract_executor import AbstractExecutor
from poly_llm.to_test.closest_integer import  closest_integer
from poly_llm.to_test.file_name_check import file_name_check
from poly_llm.to_test.numerical_letter_grade import  numerical_letter_grade
from poly_llm.to_test.find_closest_elements import  find_closest_elements
from poly_llm.to_test.separate_paren_groups import separate_paren_groups

from poly_llm.to_test.q_2_2.test_closest_integer import  test_closest_integer
from poly_llm.to_test.q_2_2.test_file_name_check import test_file_name_check
from poly_llm.to_test.q_2_2.test_separate_paren_groups import test_separate_paren_groups
from poly_llm.to_test.q_2_2.test_find_closest_elements import test_find_closest_elements
from poly_llm.to_test.q_2_2.test_numerical_letter_grade import test_numerical_letter_grade


closest_integer_executor  = AbstractExecutor(test_closest_integer)
file_name_check_executor = AbstractExecutor(test_file_name_check)
numerical_letter_grade_executor = AbstractExecutor(test_numerical_letter_grade)
find_closest_elements_executor = AbstractExecutor(test_find_closest_elements)
separate_paren_groups_executor = AbstractExecutor(test_separate_paren_groups)

closest_integer_executor._execute_input(closest_integer)
file_name_check_executor._execute_input(file_name_check)
numerical_letter_grade_executor._execute_input(numerical_letter_grade)
find_closest_elements_executor._execute_input(find_closest_elements)
separate_paren_groups_executor._execute_input(separate_paren_groups)


print(f"Closest integer : {closest_integer_executor.execution_data['coverage']}")
print(f"File name checker : {file_name_check_executor.execution_data['coverage']}")
print(f"Numerical letter grade  : {closest_integer_executor.execution_data['coverage']}")
print(f"Find closest elements : {find_closest_elements_executor.execution_data['coverage']}")
print(f"Separate paren groups : {separate_paren_groups_executor.execution_data['coverage']}")