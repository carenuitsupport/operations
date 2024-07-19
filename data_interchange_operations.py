from config_manager.closedloop_config_loader import (
    get_closedloop_cloud_provider,
    get_closedloop_password,
    get_closedloop_username,
)
from config_manager.sftp_config_loader import (
    get_hostname_acclivity_sftp_credential,
    get_port_acclivity_sftp_credential,
    get_pwd_acclivity_sftp_credential,
    get_user_acclivity_sftp_credential,
)
from closedloop.api import ClosedLoopClient
from log_manager import setup
import paramiko
from pathlib import Path

logger = setup.get_logger(__name__)


def upload_file_to_closedloop(file_name):

    cl_username = get_closedloop_username()
    cl_password = get_closedloop_password()
    cl_cloudProvider = get_closedloop_cloud_provider()

    cl = ClosedLoopClient(
        True,
        cl_username,
        cl_password,
        "https://apps.closedloop.ai",
        cl_cloudProvider,
        False,
    )

    with open(file_name, "rb") as f:

        try:
            cl.uploadFile(f, Path(file_name).name)

        except Exception as e:
            logger.error(
                f"An unexpected error ocurred when trying to upload {file_name} to ClosedLoop: {e}",
                exc_info=True,
            )


def set_acclivity_sftp_conn():

    sftp_username = get_user_acclivity_sftp_credential()
    sftp_password = get_pwd_acclivity_sftp_credential()
    sftp_hostname = get_hostname_acclivity_sftp_credential()
    sftp_port = get_port_acclivity_sftp_credential()

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        hostname=sftp_hostname,
        port=sftp_port,
        username=sftp_username,
        password=sftp_password,
    )

    return client
