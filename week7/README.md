# To-Do List Web Application

A simple Django web application for managing tasks with full CRUD functionality.

## Features

- ✓ Create new tasks with title and optional description
- ✓ View all tasks in a paginated list
- ✓ Edit task details and mark as completed
- ✓ Toggle task completion status
- ✓ Delete tasks with confirmation dialog
- ✓ Visual distinction between completed and pending tasks
- ✓ Task statistics (total, completed, remaining)
- ✓ Admin interface for task management
- ✓ Responsive design with modern UI

## Project Structure

```
week7/
├── manage.py                          # Django management script
├── requirements.txt                   # Python dependencies
├── README.md                          # This file
├── db.sqlite3                         # SQLite database (created after migration)
│
├── todoproject/                       # Main project configuration
│   ├── __init__.py
│   ├── settings.py                   # Project settings
│   ├── urls.py                       # Main URL routing
│   └── wsgi.py                       # WSGI configuration
│
├── tasks/                            # Task management app
│   ├── migrations/                   # Database migrations
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   ├── __init__.py
│   ├── admin.py                      # Admin interface configuration
│   ├── apps.py                       # App configuration
│   ├── forms.py                      # Task forms
│   ├── models.py                     # Task model
│   ├── urls.py                       # App URL routing
│   └── views.py                      # View functions and classes
│
└── templates/                        # HTML templates
    ├── base.html                     # Base template with styling
    └── tasks/
        ├── task_list.html            # Task list display
        ├── task_form.html            # Create/Edit task form
        └── task_confirm_delete.html  # Delete confirmation page
```

## Task Model Fields

- **title** (CharField): Task title (required, max 200 characters)
- **description** (TextField): Detailed task description (optional)
- **is_completed** (BooleanField): Completion status (default: False)
- **created_at** (DateTimeField): Automatic timestamp when created
- **updated_at** (DateTimeField): Automatic timestamp when modified

## URL Routes

| Route | View | Description |
|-------|------|-------------|
| `/` | TaskListView | Display all tasks |
| `/create/` | TaskCreateView | Create a new task |
| `/<id>/edit/` | TaskUpdateView | Edit existing task |
| `/<id>/delete/` | TaskDeleteView | Delete task with confirmation |
| `/<id>/toggle/` | TaskToggleView | Toggle task completion |
| `/admin/` | Django Admin | Admin interface |

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Apply Migrations
```bash
python manage.py migrate
```

### 3. Create Superuser (Optional)
To access the admin interface:
```bash
python manage.py createsuperuser
```

### 4. Run the Development Server
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Usage

### Creating a Task
1. Click the **"+ New Task"** button
2. Enter the task title (required)
3. Optionally add a description
4. Click **"Create Task"**

### Editing a Task
1. Click the **"Edit"** button on any task
2. Modify the title, description, or mark as completed
3. Click **"Update Task"**

### Completing a Task
1. Click the **"Complete"** button on a pending task
2. The task will be marked as completed with strikethrough text
3. Click **"Undo"** to revert completion status

### Deleting a Task
1. Click the **"Delete"** button on any task
2. Review the confirmation message
3. Click **"Yes, Delete Task"** to confirm

## Admin Interface

Access the admin panel at `/admin/` with your superuser credentials to:
- Manage tasks directly
- Filter tasks by completion status and date
- Search tasks by title or description
- View and edit task metadata

## Styling

The application features:
- Modern gradient background
- Clean card-based layout
- Color-coded status indicators
- Responsive design for mobile devices
- Smooth transitions and hover effects
- Accessible form elements

## Validation

The form includes:
- Required title field validation
- Optional description field
- Automatic timestamp management
- Secure CSRF token protection

## Notes

- Tasks are sorted by creation date (newest first)
- Completed tasks are visually distinguished with strikethrough text
- The application uses SQLite for development
- For production, update the SECRET_KEY and consider using PostgreSQL
