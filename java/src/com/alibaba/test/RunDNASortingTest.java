package com.alibaba.test;

import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.LineNumberReader;

import org.apache.commons.lang.StringUtils;

public class RunDNASortingTest {

    private static final String BLANK                = " ";

    private static final String TEN_SIX_CASE         = "com/alibaba/test/106.testcase";
    private static final String TEN_SIX_RESULT       = "com/alibaba/test/106.result";

    private static final String TEN_TEN_CASE         = "com/alibaba/test/1010.testcase";
    private static final String TEN_TEN_RESULT       = "com/alibaba/test/1010.result";

    private static final String FIFTY_HUNDRED_CASE   = "com/alibaba/test/50100.testcase";
    private static final String FIFTY_HUNDRED_RESULT = "com/alibaba/test/50100.result";

    public static void main(String[] args) throws IOException, InterruptedException {
        if (args == null || (args.length != 2 && args.length != 4)) {
            throw new IllegalArgumentException("argument error");
        }

        if ("java".equals(args[0])) {
            callAndMeasure("java -classpath " + args[2], args[3]);
        } else if ("shell".equals(args[0])) {
            callAndMeasure("/bin/sh", args[1]);
        } else if ("python".equals(args[0])) {
            callAndMeasure("python", args[1]);
        }

    }

    private static void callAndMeasure(String programCommand, String programName) throws IOException,
                                                                                 InterruptedException {
        String tenSixResult = exe(programCommand, programName, getStringFromFile(TEN_SIX_CASE));
        checkResult(TEN_SIX_CASE, tenSixResult, getStringFromFile(TEN_SIX_RESULT));
        String twentyFiftyResult = exe(programCommand, programName, getStringFromFile(TEN_TEN_CASE));
        checkResult(TEN_TEN_CASE, twentyFiftyResult, getStringFromFile(TEN_TEN_RESULT));

        long timeBegin = System.currentTimeMillis();
        String fiftyHundredResult = exe(programCommand, programName, getStringFromFile(FIFTY_HUNDRED_CASE));
        checkResult(FIFTY_HUNDRED_CASE, fiftyHundredResult, getStringFromFile(FIFTY_HUNDRED_RESULT));
        System.out.println("sucess and cost in mili seconds: " + (System.currentTimeMillis() - timeBegin));
    }

    private static String getStringFromFile(String result) throws IOException {
        InputStream in = Thread.currentThread().getContextClassLoader().getSystemResource(result).openStream();

        LineNumberReader numberBuffer = new LineNumberReader(new InputStreamReader(in));

        StringBuilder builder = new StringBuilder();
        String input;
        while ((input = numberBuffer.readLine()) != null) {
            builder.append(input.trim()).append(BLANK);
        }
        return builder.toString().trim();
    }

    private static void checkResult(String input, String tenSixResult, String tenSixResult2) {

        String result[] = StringUtils.split(tenSixResult, BLANK);
        String result2[] = StringUtils.split(tenSixResult2, BLANK);

        if (result.length != result2.length) {
            System.out.println(result.length + " : " + result2.length);
            throw new RuntimeException("result not right in the case of : " + input + " , the result is: "
                                       + tenSixResult);
        }

        for (int i = 0; i < result.length; i++) {
            if (result[i].trim().equals(result2[i].trim())) {

            } else {
                System.out.println("index " + i + "not match : " + result[i] + " " + result2[i]);
                throw new RuntimeException("result not right in the case of : " + input + " , the result is: "
                                           + tenSixResult);
            }
        }

    }

    private static String exe(String programType, String programName, String parameters) throws IOException,
                                                                                        InterruptedException {
        Process process = Runtime.getRuntime().exec(programType + BLANK + programName + BLANK + parameters);

        process.waitFor();

        InputStreamReader irError = new InputStreamReader(process.getErrorStream());
        LineNumberReader errorStreamReader = new LineNumberReader(irError);
        StringBuilder resultErrorBuilder = new StringBuilder();
        String resultError;
        while ((resultError = errorStreamReader.readLine()) != null) {
            resultErrorBuilder.append(resultError);
        }

        if (resultErrorBuilder.toString() != null && !resultErrorBuilder.toString().isEmpty()) {
            throw new RuntimeException(resultErrorBuilder.toString());
        }
        InputStreamReader ir = new InputStreamReader(process.getInputStream());
        LineNumberReader infoStreamReader = new LineNumberReader(ir);
        StringBuilder resultInfoBuilder = new StringBuilder();
        String resultInfo;
        while ((resultInfo = infoStreamReader.readLine()) != null) {
            resultInfoBuilder.append(resultInfo.trim()).append(BLANK);
        }

        return resultInfoBuilder.toString().trim();
    }
}
