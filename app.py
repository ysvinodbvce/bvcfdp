"""Simple CLI to collect subject marks, compute percentage and grade."""

def get_grade(pct: float) -> str:
	if pct >= 90:
		return 'A+'
	if pct >= 80:
		return 'A'
	if pct >= 70:
		return 'B'
	if pct >= 60:
		return 'C'
	if pct >= 50:
		return 'D'
	return 'F'


def prompt_positive_int(prompt: str) -> int:
	while True:
		try:
			v = int(input(prompt).strip())
			if v > 0:
				return v
			print('Please enter a positive integer.')
		except ValueError:
			print('Invalid input. Please enter a positive integer.')


def prompt_marks(prompt: str) -> float:
	while True:
		try:
			v = float(input(prompt).strip())
			if 0 <= v <= 100:
				return v
			print('Marks must be between 0 and 100.')
		except ValueError:
			print('Invalid input. Enter a number between 0 and 100.')


def main():
	print('Student Percentage & Grade Calculator (CLI)')
	n = prompt_positive_int('Number of subjects: ')

	subjects = []
	total = 0.0
	for i in range(1, n + 1):
		name = input(f'Name of subject {i} (press Enter to skip): ').strip() or f'Subject {i}'
		marks = prompt_marks(f'Enter marks for "{name}" (0-100): ')
		subjects.append((name, marks))
		total += marks

	max_total = n * 100
	percentage = (total / max_total) * 100 if max_total > 0 else 0.0
	grade = get_grade(percentage)

	print('\n--- Result ---')
	print(f'Total: {total:.2f} / {max_total:.2f}')
	print(f'Percentage: {percentage:.2f}%')
	print(f'Grade: {grade}')
	print('\nBreakdown:')
	for name, marks in subjects:
		print(f' - {name}: {marks:.2f} / 100 ({marks:.2f}%)')


if __name__ == '__main__':
	main()

