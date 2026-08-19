job "hello-devops" {
  datacenters = ["dc1"]
  type        = "service"

  group "web" {
    count = 1

    restart {
      attempts = 3
      interval = "10m"
      delay    = "15s"
      mode     = "delay"
    }

    task "hello-runner" {
      driver = "docker"

      config {
        image = "hello-devops:latest"
      }

      resources {
        cpu    = 100 # MHz (minimal allocation)
        memory = 64  # MB (minimal allocation)
      }

      service {
        name = "hello-service"
        tags = ["devops", "intern-assessment"]
      }
    }
  }
}
