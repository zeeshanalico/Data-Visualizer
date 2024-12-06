create type ACC_STATUS as enum ( 'active', 'inactive', 'archived' );
CREATE TABLE public.user (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    tel_no VARCHAR(255),
    location VARCHAR(255),
    website VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(255),
    zip_code VARCHAR(255),
    category VARCHAR(255),
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    is_deleted BOOLEAN,
    is_dummy BOOLEAN,
    acc_status acc_status,
    created_by VARCHAR(255),
    deleted_by VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP
);
