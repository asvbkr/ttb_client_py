# coding: utf-8

"""
    TamTam Bot API

    # About Bot API allows bots to interact with TamTam. Methods are called by sending HTTPS requests to [botapi.tamtam.chat](https://botapi.tamtam.chat) domain. Bots are third-party applications that use TamTam features. A bot can legitimately take part in a conversation. It can be achieved through HTTP requests to the TamTam Bot API.  ## Features TamTam bots of the current version are able to: - Communicate with users and respond to requests - Recommend users complete actions via programmed buttons - Request personal data from users (name, short reference, phone number) We'll keep working on expanding bot capabilities in the future.  ## Examples Bots can be used for the following purposes: - Providing support, answering frequently asked questions - Sending typical information - Voting - Likes/dislikes - Following external links - Forwarding a user to a chat/channel  ## @PrimeBot [PrimeBot](https://tt.me/primebot) is the main bot in TamTam, all bots creator. Use PrimeBot to create and edit your bots. Feel free to contact us for any questions, [@support](https://tt.me/support) or [team@tamtam.chat](mailto:team@tamtam.chat).  #### [PrimeBot](https://tt.me/primebot) commands: `/start` &mdash; start a dialog with a bot  `/create` &mdash; create a bot, assign the unique short name to it (from 4 to 64 characters)  `/set_name [name]` &mdash; assign a short or full name to the bot (up to 200 characters)  `/set_description [description]` &mdash; enter the description for the bot profile (up to 400 characters)  `/set_picture [URL]` &mdash; enter the URL of bot's picture  `/delete [username]` &mdash; delete the bot  `/list` &mdash; show the list of all bots  `/get_token` &mdash; obtain a token for a bot  `/revoke` &mdash; request a new token  `/help` &mdash; help  ## HTTP verbs `GET` &mdash; getting resources, parameters are transmitted via URL  `POST` &mdash; creation of resources (for example, sending new messages)  `PUT` &mdash; editing resources  `DELETE` &mdash; deleting resources  `PATCH` &mdash; patching resources  ## HTTP response codes `200` &mdash; successful operation  `400` &mdash; invalid request  `401` &mdash; authentication error  `404` &mdash; resource not found  `405` &mdash; method is not allowed  `429` &mdash; the number of requests is exceeded  `503` &mdash; service unavailable  ## Resources format For content requests (PUT and POST) and responses, the API uses the JSON format. All strings are UTF-8 encoded. Date/time fields are represented as the number of milliseconds that have elapsed since 00:00 January 1, 1970 in the long format. To get it, you can simply multiply the UNIX timestamp by 1000. All date/time fields have a UTC timezone. ## Error responses In case of an error, the API returns a response with the corresponding HTTP code and JSON with the following fields:  `code` - the string with the error key  `message` - a string describing the error </br>  For example: ```bash > http https://botapi.tamtam.chat/chats?access_token={EXAMPLE_TOKEN} HTTP / 1.1 403 Forbidden Cache-Control: no-cache Connection: Keep-Alive Content-Length: 57 Content-Type: application / json; charset = utf-8 Set-Cookie: web_ui_lang = ru; Path = /; Domain = .tamtam.chat; Expires = 2019-03-24T11: 45: 36.500Z {    \"code\": \"verify.token\",    \"message\": \"Invalid access_token\" } ``` ## Receiving Notifications TamTam Bot API supports 2 options of receiving notifications on new dialog events for bots: - Push notifications via WebHook. To receive data via WebHook, you'll have to [add subscription](https://dev.tamtam.chat/#operation/subscribe); - Notifications upon request via [long polling](#operation/getUpdates) API. All data can be received via long polling **by default** after creating the bot,  Both methods **cannot** be used simultaneously. Refer to the response schema of [/updates](https://dev.tamtam.chat/#operation/getUpdates) method to check all available types of updates.  ## Message buttons You can program buttons for users answering a bot. TamTam supports the following types of buttons:  `callback` &mdash; sends a notification to a bot (via WebHook or long polling)  `link` &mdash; makes a user to follow a link  `request_contact` &mdash; requests the user permission to access contact information (phone number, short link, email)  You may also send a message with an [InlineKeyboard]() type attachment to start creating buttons. When the user presses a button, the bot receives the answer with filled callback field. It is recommended to edit that message so the user can receive updated buttons.  # Versioning API models and interface may change over time. To make sure your bot will get the right info, we strongly recommend adding API version number to each request. You can add it as `v` parameter to each HTTP-request. For instance, `v=0.1.2`. To specify the data model version you are getting through WebHook subscription, use the `version` property in the request body of the [subscribe](https://dev.tamtam.chat/#operation/subscribe) request.  # Libraries We have created [Java library](https://github.com/tamtam-chat/tamtam-bot-api) to make using API easier.  # Changelog ##### Version 0.1.8 - Added `code`, `width`, `height` to [StickerAttachment](https://github.com/tamtam-chat/tamtam-bot-api-schema/blob/master/schema.yaml#L1580) - `token` is now only one required property for video/audio/file attachments - `sender` and `chat_id` of [LinkedMessage](https://github.com/tamtam-chat/tamtam-bot-api-schema/blob/master/schema.yaml#L1401) are now optional - Added clarifying `message` to [SimpleQueryResult](https://github.com/tamtam-chat/tamtam-bot-api-schema/blob/master/schema.yaml#L1938)  ##### Version 0.1.7 - It is now **required** to pass `marker` parameter in [/updates](#operation/getUpdates) requests, except initial - Added full `User` object to update types: bot_started, bot_added, bot_removed, user_added, user_removed, chat_title_changed - Added `size` and `filename` to [`FileAttachment`](https://github.com/tamtam-chat/tamtam-bot-api-schema/blob/master/schema.yaml#L1503) - Added [`token`](https://github.com/tamtam-chat/tamtam-bot-api-schema/blob/master/schema.yaml#L1525) property to video/audio/file attachments allows you to reuse attachments uploaded by another user  ##### Version 0.1.6 - Added method to [edit bot info](#operation/editMyInfo) - Added statistics for messages in channel - `Message.sender` and `UserWithPhoto.avatar_url/full_avatar_url` removed from required properties  ##### Version 0.1.5 - Added `id` property to media attachments (`VideoAttachment`, `AudioAttachment`) so you can reuse attachment from one message in another - Added ability to create *linked* message: replied or forwarded. See `link` in `NewMessageBody` - `intent` property marked as required only for `CallbackButton`  ##### Version 0.1.4 - Added `user_ids` parameter to [get members](#operation/getMembers) in chat by id - `attachment` property of [send message](#operation/sendMessage) request body marked as deprecated  ##### Version 0.1.3 - Added method to [delete](https://dev.tamtam.chat/#operation/deleteMessages) messages - Added ability to [get](https://dev.tamtam.chat/#operation/getMessages) particular messages by ID - Added `is_admin` flag to `ChatMember` - Added `message` property to `MessageCallbackUpdate` - Renamed property `message` to `body` for `Message` schema - Added reusable `token` to `PhotoAttachment`. It allows to attach the same photo more than once.  # noqa: E501

    OpenAPI spec version: 0.1.9
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six


class NewMessageBody(object):
    MAX_BODY_LENGTH = 4000
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'text': 'str',
        'attachment': 'AttachmentRequest',
        'attachments': 'list[AttachmentRequest]',
        'link': 'NewMessageLink',
        'notify': 'bool'
    }

    attribute_map = {
        'text': 'text',
        'attachment': 'attachment',
        'attachments': 'attachments',
        'link': 'link',
        'notify': 'notify'
    }

    def __init__(self, text=None, attachment=None, attachments=None, link=None, notify=True):  # noqa: E501
        """NewMessageBody - a model defined in OpenAPI"""  # noqa: E501

        self._text = None
        self._attachment = None
        self._attachments = None
        self._link = None
        self._notify = None
        self.discriminator = None

        self.text = text
        self.attachment = attachment
        self.attachments = attachments
        self.link = link
        if notify is not None:
            self.notify = notify

    @property
    def text(self):
        """Gets the text of this NewMessageBody.  # noqa: E501

        Message text  # noqa: E501

        :return: The text of this NewMessageBody.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this NewMessageBody.

        Message text  # noqa: E501

        :param text: The text of this NewMessageBody.  # noqa: E501
        :type: str
        """
        if text is not None and len(text) > self.MAX_BODY_LENGTH:
            raise ValueError("Invalid value for `text`, length must be less than or equal to `%s`" % self.MAX_BODY_LENGTH)  # noqa: E501

        self._text = text

    @property
    def attachment(self):
        """Gets the attachment of this NewMessageBody.  # noqa: E501

        Use `attachments` property instead. Will be removed in the next major release.  Single message attachment  # noqa: E501

        :return: The attachment of this NewMessageBody.  # noqa: E501
        :rtype: AttachmentRequest
        """
        return self._attachment

    @attachment.setter
    def attachment(self, attachment):
        """Sets the attachment of this NewMessageBody.

        Use `attachments` property instead. Will be removed in the next major release.  Single message attachment  # noqa: E501

        :param attachment: The attachment of this NewMessageBody.  # noqa: E501
        :type: AttachmentRequest
        """

        self._attachment = attachment

    @property
    def attachments(self):
        """Gets the attachments of this NewMessageBody.  # noqa: E501

        Message attachments. See `AttachmentRequest` and it's inheritors for full information  # noqa: E501

        :return: The attachments of this NewMessageBody.  # noqa: E501
        :rtype: list[AttachmentRequest]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this NewMessageBody.

        Message attachments. See `AttachmentRequest` and it's inheritors for full information  # noqa: E501

        :param attachments: The attachments of this NewMessageBody.  # noqa: E501
        :type: list[AttachmentRequest]
        """

        self._attachments = attachments

    @property
    def link(self):
        """Gets the link of this NewMessageBody.  # noqa: E501

        Link to Message  # noqa: E501

        :return: The link of this NewMessageBody.  # noqa: E501
        :rtype: NewMessageLink
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this NewMessageBody.

        Link to Message  # noqa: E501

        :param link: The link of this NewMessageBody.  # noqa: E501
        :type: NewMessageLink
        """

        self._link = link

    @property
    def notify(self):
        """Gets the notify of this NewMessageBody.  # noqa: E501

        If false, chat participants wouldn't be notified  # noqa: E501

        :return: The notify of this NewMessageBody.  # noqa: E501
        :rtype: bool
        """
        return self._notify

    @notify.setter
    def notify(self, notify):
        """Sets the notify of this NewMessageBody.

        If false, chat participants wouldn't be notified  # noqa: E501

        :param notify: The notify of this NewMessageBody.  # noqa: E501
        :type: bool
        """

        self._notify = notify

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NewMessageBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
