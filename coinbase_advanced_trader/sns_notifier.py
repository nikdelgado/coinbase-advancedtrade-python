import boto3
import logging

logger = logging.getLogger(__name__)

class SNSNotifier:
    def __init__(self, sns_topic_arn):
        self.sns_client = boto3.client('sns')
        self.sns_topic_arn = sns_topic_arn

    def send_notification(self, subject, message):
        """
        Sends an SNS notification.
        :param subject: Subject of the notification
        :param message: Message content
        """
        try:
            response = self.sns_client.publish(
                TopicArn=self.sns_topic_arn,
                Subject=subject,
                Message=message
            )
            logger.info(f"SNS Notification sent successfully: {response}")
            return response
        except Exception as e:
            logger.error(f"Failed to send SNS notification: {str(e)}")
            return None