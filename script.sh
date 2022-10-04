# Scale vertival SQL Instance vCPUs & memory
# gcloud sql instances patch percobaan --cpu=2 --memory=3840MiB => Scale Down
# gcloud sql instances patch percobaan --cpu=8 --memory=7424MiB => Scale Up
set -e

while [ $# -gt 0 ]; do
  case "$1" in
     -i=* | --instance=*)
      instance="${1#*=}"
      ;;
    -p=* | --project=*)
      project="${1#*=}"
      ;;
    -z=* | --zone=*)
      zone="${1#*=}"
      ;;
    -c=* | --cpu=*)
      cpu="${1#*=}"
      ;;
    -m=* | --memory=*)
      memory="${1#*=}"
      ;;
    *)
      printf "Error: unknown option: $1\n"
      exit 1
  esac
  shift
done

echo Execution!
gcloud sql instances patch $instance --project=$project  --cpu=$cpu --memory=$memory
echo All done!