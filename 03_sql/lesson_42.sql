CREATE TABLE tasks (
    id INTEGER,
    title TEXT,
    is_completed BOOLEAN
);

INSERT INTO tasks (
    id,
    title,
    is_completed
)
VALUES (
    1,
    'Learn PostgreSQL',
    FALSE
);

INSERT INTO tasks (
    id,
    title,
    is_completed
)
VALUES (
    2,
    'Learn SQL',
    FALSE
);

INSERT INTO tasks (
    id,
    title,
    is_completed
)
VALUES (
    3,
    'Build Task Manager',
    TRUE
);

SELECT * FROM tasks;