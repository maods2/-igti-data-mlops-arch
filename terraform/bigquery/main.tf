resource "google_sql_database_instance" "postgres" {
  project          = "projeto-final-xp"
  name             = "igti-mlops-db"
  database_version = "POSTGRES_14"
  region           = "us-central1"

  settings {
    # Second-generation instance tiers are based on the machine
    # type. See argument reference below.
    tier = "db-f1-micro"
  }

}

resource "google_sql_database" "database" {
  project  = "projeto-final-xp"
  name     = "finance_db"
  instance = google_sql_database_instance.postgres.name
}


resource "google_sql_user" "users" {
  project  = "projeto-final-xp"
  name     = "admin"
  instance = google_sql_database_instance.postgres.name
  password = "senha@123"
}
