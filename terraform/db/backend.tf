terraform {
 backend "gcs" {
   bucket  = "igti-bucket-tfstate"
   prefix  = "terraform/db"
 }
}