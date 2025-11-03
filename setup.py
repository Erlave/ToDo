from setuptools import setup, find_packages

setup(
    name="erlave-todo",                   # اسم پکیج
    version="0.1.0",                      # نسخه
    description="CLI Todo app by Erlave",
    author="Erlave",
    packages=find_packages(where="src"),  # پکیج‌ها رو از src پیدا کن
    package_dir={"": "src"},              # پوشه مبدا کدها
    install_requires=[
        "colorama",
        "tabulate",
    ],
    entry_points={
        "console_scripts": [
            "todo = todo.main:main",      # دستور CLI: todo → تابع main در todo/main.py
        ],
    },
    python_requires=">=3.8",
)
