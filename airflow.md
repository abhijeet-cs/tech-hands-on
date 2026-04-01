# 🌪️ Airflow Notes

## 🧭 What is Airflow
**Airflow** is a **workflow orchestration platform** used to schedule, manage, and monitor pipelines.

---

## ⚙️ Core Components

| Component | Responsibility |
|---|---|
| 🗄️ **Metadata DB** | Source of truth (task state, configs, DAG metadata) |
| ⏰ **Scheduler** | Decides **when** tasks should run |
| 🚀 **Executor** | Decides **how / where** tasks run |
| 📬 **Queue** | Stores tasks waiting for execution |
| 📄 **DAG File Processor** | Parses DAG files → serializes into DB |
| 👷 **Worker** | Executes actual tasks |
| 🔔 **Triggerer** | Handles async waiting (deferrable / non-blocking tasks) |

---

## 🧩 Operators
**Operators** define the **type of work** performed by a task.

Examples:
- PythonOperator
- BashOperator
- SQL Operators
- Sensors

---

## 🏗️ Multinode Architecture (Execution Flow)

### 1️⃣ API Server
- Interface to Metadata DB
- Used by UI, workers, and triggerer

### 2️⃣ DAG Processors
- Parse DAG files
- Store serialized DAGs in DB

### 3️⃣ Scheduler + Executor
- Read task metadata from DB
- Push runnable tasks into Queue

### 4️⃣ Workers
- Pull tasks from Queue
- Execute tasks
- Update status via API Server

---

## 🔌 Operator Configuration

If a **connection type** is missing in Airflow UI:

Install the required provider:

```bash
pip install apache-airflow-providers-<provider>
```

## 🎯 Priority-Based Queues
Priority-based queues allow routing tasks to **specific workers** based on workload, priority, or resource needs.
### Step 1️⃣ Configure Worker Queues:
```bash
airflow celery worker -q high_priority,default
```
### Step 2️⃣ Assign Queue to Task
```bash
task = PythonOperator(
    task_id="important_task",
    queue="high_priority",
)
```


