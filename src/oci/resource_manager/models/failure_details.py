# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FailureDetails(object):
    """
    FailureDetails model.
    """

    #: A constant which can be used with the code property of a FailureDetails.
    #: This constant has a value of "INTERNAL_SERVICE_ERROR"
    CODE_INTERNAL_SERVICE_ERROR = "INTERNAL_SERVICE_ERROR"

    #: A constant which can be used with the code property of a FailureDetails.
    #: This constant has a value of "TERRAFORM_EXECUTION_ERROR"
    CODE_TERRAFORM_EXECUTION_ERROR = "TERRAFORM_EXECUTION_ERROR"

    #: A constant which can be used with the code property of a FailureDetails.
    #: This constant has a value of "TERRAFORM_CONFIG_UNZIP_FAILED"
    CODE_TERRAFORM_CONFIG_UNZIP_FAILED = "TERRAFORM_CONFIG_UNZIP_FAILED"

    #: A constant which can be used with the code property of a FailureDetails.
    #: This constant has a value of "INVALID_WORKING_DIRECTORY"
    CODE_INVALID_WORKING_DIRECTORY = "INVALID_WORKING_DIRECTORY"

    #: A constant which can be used with the code property of a FailureDetails.
    #: This constant has a value of "JOB_TIMEOUT"
    CODE_JOB_TIMEOUT = "JOB_TIMEOUT"

    #: A constant which can be used with the code property of a FailureDetails.
    #: This constant has a value of "TERRAFORM_CONFIG_VIRUS_FOUND"
    CODE_TERRAFORM_CONFIG_VIRUS_FOUND = "TERRAFORM_CONFIG_VIRUS_FOUND"

    def __init__(self, **kwargs):
        """
        Initializes a new FailureDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param code:
            The value to assign to the code property of this FailureDetails.
            Allowed values for this property are: "INTERNAL_SERVICE_ERROR", "TERRAFORM_EXECUTION_ERROR", "TERRAFORM_CONFIG_UNZIP_FAILED", "INVALID_WORKING_DIRECTORY", "JOB_TIMEOUT", "TERRAFORM_CONFIG_VIRUS_FOUND", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type code: str

        :param message:
            The value to assign to the message property of this FailureDetails.
        :type message: str

        """
        self.swagger_types = {
            'code': 'str',
            'message': 'str'
        }

        self.attribute_map = {
            'code': 'code',
            'message': 'message'
        }

        self._code = None
        self._message = None

    @property
    def code(self):
        """
        **[Required]** Gets the code of this FailureDetails.
        Job failure reason.

        Allowed values for this property are: "INTERNAL_SERVICE_ERROR", "TERRAFORM_EXECUTION_ERROR", "TERRAFORM_CONFIG_UNZIP_FAILED", "INVALID_WORKING_DIRECTORY", "JOB_TIMEOUT", "TERRAFORM_CONFIG_VIRUS_FOUND", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The code of this FailureDetails.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this FailureDetails.
        Job failure reason.


        :param code: The code of this FailureDetails.
        :type: str
        """
        allowed_values = ["INTERNAL_SERVICE_ERROR", "TERRAFORM_EXECUTION_ERROR", "TERRAFORM_CONFIG_UNZIP_FAILED", "INVALID_WORKING_DIRECTORY", "JOB_TIMEOUT", "TERRAFORM_CONFIG_VIRUS_FOUND"]
        if not value_allowed_none_or_none_sentinel(code, allowed_values):
            code = 'UNKNOWN_ENUM_VALUE'
        self._code = code

    @property
    def message(self):
        """
        **[Required]** Gets the message of this FailureDetails.
        A human-readable error string.


        :return: The message of this FailureDetails.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this FailureDetails.
        A human-readable error string.


        :param message: The message of this FailureDetails.
        :type: str
        """
        self._message = message

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other