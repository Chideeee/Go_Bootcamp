# Service Account
resource "google_service_account" "vm-sa" {
  account_id   = "vm-sa"
  display_name = "VM Service Account"
}

resource "google_project_iam_member" "vm-iam" {
  project = "my-gcp-project
  role    = "roles/container.admin"
  member  = "serviceAccount:${google_service_account.vm-sa.email}"
}
# Firewall
resource "google_compute_firewall" "allow-http" {
  name = "allow-http"
  
  # attach to your own VPC
  network = google_compute_network.default.name
  allow {
    protocol = "tcp"
    ports = [ "80", "443" ]
  }
  source_ranges = ["0.0.0.0/0"]
  target_tags = ["http-server"]
}
# Sentry VM
resource "google_compute_instance" "sentry-vm" {
  name         = "sentry-vm"
  machine_type = "custom-4-16000"
  zone         = "asia-southeast2-a"
  tags = ["http-server"]
  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-2204-lts"
      size = 80
      type = "pd-balanced"
    }
  }
  network_interface {
    # attach to your own subnetwork
    subnetwork = google_compute_subnetwork.main.self_link
    
    # Get Public IP Address
    access_config {}
  }
  service_account {
    email  = google_service_account.vm-sa.email
    scopes = ["cloud-platform"]
  }
}