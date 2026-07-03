-- ==========================================
-- CARE AI Solution Engine
-- Database Schema
-- ==========================================

DROP TABLE IF EXISTS problems;
DROP TABLE IF EXISTS job_details;
DROP TABLE IF EXISTS solutions;
DROP TABLE IF EXISTS kb_articles;
DROP TABLE IF EXISTS historical_incidents;


-- ==========================================
-- Problems
-- ==========================================

CREATE TABLE problems (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    problem_id TEXT UNIQUE,

    job_instance_id TEXT,

    client_code TEXT,

    client_name TEXT,

    property_code TEXT,

    property_name TEXT,

    job_name TEXT,

    step_name TEXT,

    owner TEXT,

    system_mode TEXT,

    creation_date TEXT,

    closed_date TEXT,

    duration TEXT,

    error_code TEXT,

    node TEXT,

    problem_description TEXT

);


-- ==========================================
-- Job Details
-- ==========================================

CREATE TABLE job_details (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    problem_id TEXT,

    step_name TEXT,

    status TEXT,

    start_date TEXT,

    end_date TEXT,

    duration TEXT,

    value TEXT,

    log_available INTEGER DEFAULT 0

);


-- ==========================================
-- Existing Solutions
-- ==========================================

CREATE TABLE solutions (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    error_code TEXT,

    title TEXT,

    solution TEXT,

    created_by TEXT,

    created_date TEXT

);


-- ==========================================
-- Knowledge Base
-- ==========================================

CREATE TABLE kb_articles (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    kb_number TEXT,

    title TEXT,

    category TEXT,

    content TEXT,

    source TEXT

);


-- ==========================================
-- Historical Incidents
-- ==========================================

CREATE TABLE historical_incidents (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    problem_id TEXT,

    error_code TEXT,

    root_cause TEXT,

    resolution TEXT,

    kb_reference TEXT,

    resolved_by TEXT,

    resolved_date TEXT

);